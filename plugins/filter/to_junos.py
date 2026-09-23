#!/usr/bin/python

# Copyright (c) 2026, Bryant A
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
# SPDX-License-Identifier: MIT

from __future__ import annotations

DOCUMENTATION = r"""
name: to_junos
short_description: Render structured data into Junos block syntax
description:
  - Takes a nested dictionary/list structure and renders it into Junos configuration syntax with proper indentation and curly braces.
author:
  - Bryant A (@iambryant)
requirements:
  - Junos OS
options:
  _input:
    description: Dictionary containing configuration structure.
    type: dict
    required: true
"""

EXAMPLES = r"""
- name: Render Junos configuration block
  ansible.builtin.debug:
    msg: "{{ junos_config | to_junos }}"
  vars:
    junos_config:
      system:
        host-name: core-router-01
        domain-name: lab.net
        services:
          ssh:
          netconf:
            ssh:
              port: 830
      interfaces:
        ge-0/0/0:
          description: "Link to Core-02"
          unit 0:
            family:
              inet:
                address: 10.255.255.1/30
"""

RETURN = r"""
_value:
  description: The rendered Junos text block.
  type: str
"""

def to_junos_config(data, indent=0):
    pad = "    " * indent
    lines = []

    if not isinstance(data, dict):
        return ""

    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{key} {{")
            nested = to_junos_config(value, indent + 1)
            if nested:
                lines.append(nested)
            lines.append(f"{pad}}}")
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    lines.append(f"{pad}{key} {{")
                    nested = to_junos_config(item, indent + 1)
                    if nested:
                        lines.append(nested)
                    lines.append(f"{pad}}}")
                else:
                    lines.append(f"{pad}{key} {item};")
        elif value is not None:
            lines.append(f"{pad}{key} {value};")

    return "\n".join(lines)

class FilterModule:
    """Ansible Jinja2 Junos filter"""

    def filters(self):
        return {
            'to_junos': to_junos_config
        }
