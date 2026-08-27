# Ansible Collection: Junos

[![CI](https://github.com/iambryant/ansible-collection-junos/actions/workflows/ci.yml/badge.svg)](https://github.com/iambryant/ansible-collection-junos/actions/workflows/ci.yml)

This collection includes roles for automating common tasks in Junos OS.

## Installation

You can include this collection in your `requirements.yml` like this:

```
collections:
  - name: iambryant.junos
    source: https://github.com/iambryant/ansible-collection-junos
    type: git
```

## Requirements

This collection uses the [juniper.device](https://galaxy.ansible.com/ui/repo/published/juniper/device/docs/)
collection and requires the following packages on the control node:

  - Python >= 3.12
  - Ansible 2.17 or later
  - Junos py-junos-eznc 2.7.3 or later
  - jxmlease 1.0.1 or later
  - xmltodict 0.13.0 or later
  - jsnapy 1.3.7 or later
  - packaging 25.0 or later


## Included Roles

  - `iambryant.junos.acme` ([documentation](https://github.com/iambryant/ansible-collection-junos/blob/main/roles/acme/README.md))

## Usage

To see an example of this collection's usage, see: https://github.com/iambryant/junos-dev-playbook.

## License

MIT

## Acknowledgements

Credit goes to [laurent-jnpr](https://github.com/laurent-jnpr); I used elements from a template in their repository
[VNF-on-Juniper-NFX-with-Ansible](https://github.com/Juniper-SE/VNF-on-Juniper-NFX-with-Ansible) to build the VNF
creation template.
