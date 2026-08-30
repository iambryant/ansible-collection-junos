# Ansible Role: VNF

This role installs virtual network functions on the Juniper NFX family.

> [!NOTE]
> This role manages Linux and vSRX VNFs by default. It will download an Ubuntu 26 cloud image to `/tmp` on your control
> node to use for Linux VNFs. If you're planning on running a vSRX VNF, place the `junos-vsrx3-x86-64-23.4R2-S5.5.qcow2`
> image in `/tmp` on your control node. I should probably add support for more VNF types (VyOS, RouterOS, etc.) in the
> future.

## Requirements

Refer to the [requirements](https://github.com/iambryant/ansible-collection-junos#requirements) section in the
collection's README.

## Role Variables

    vnf_instances: []

The list of virtual network functions to be installed. Supports the following parameters:

| Parameter                 | Type       | Required | Description                                                                                                                                                                             |
| :---                      | :---       | :---     | :---                                                                                                                                                                                    |
| `name`                    | String     | **Yes**  | The name of the VNF. Also used as the hostname in cloud-init, if type set to `linux`, or juniper.conf if type set to `vsrx`.                                                            |
| `domain`                  | String     | **Yes**  | The domain name the VNF will use.                                                                                                                                                       |
| `type`                    | String     | No       | The type of VNF to create. Options are `linux` or `vsrx`. Defaults to `linux`.                                                                                                          |
| `root_authentication`     | String     | No       | The encrypted root password for the VNF. **Required if using type `vsrx`.** Defaults to `system_root_authentication` if omitted, which can be defined in `group_vars/` or `host_vars/`. |
| `mgmt_ip`                 | String     | No       | If type was set to `vsrx`, the management IP the VNF will use.                                                                                                                          |
| `mgmt_gateway`            | String     | No       | If type was set to `vsrx`, the management gateway the VNF will use.                                                                                                                     |
| `vcpu_count`              | Integer    | **Yes**  | The number of vCPUs the VNF will use.                                                                                                                                                   |
| `memory`                  | Integer    | **Yes**  | The amount of memory the VNF will use.                                                                                                                                                  |
| `vcpu_mapping`            | List       | No       | Refer to `vcpu_mapping`.                                                                                                                                                                |
| `hardware_virtualization` | Boolean    | No       | Whether or not the VNF should use hardware virtualization. Defaults to `false`.                                                                                                         |
| `hugepage`                | Boolean    | No       | Whether or not the VNF should use hugepages.                                                                                                                                            |
| `no_default_interfaces`   | Boolean    | No       | Whether or not Junos should allocate the default `eth0` and `eth1` interfaces for the VNF. Defaults to `false`.                                                                         |
| `interfaces`              | List       | No       | Refer to `interfaces`.                                                                                                                                                                  |
| `no_autostart`            | Boolean    | No       | Whether or not the VNF should start after creation/on boot. Defaults to `false`.                                                                                                        |
| `absent`                  | Boolean    | No       | Whether or not the VNF should be removed. Defaults to `false`.                                                                                                                          |
| `user_data`               | Dictionary | No       | Accepts cloud-init `user-data` configuration. **Required if using type `linux`.**                                                                                                       |
| `network_config`          | Dictionary | No       | Accepts cloud-init `network-config` configuration. **Required if using type `linux`.**                                                                                                  |

### vcpu_mapping

| Parameter      | Type    | Required | Description                                                                                  |
| :---           | :---    | :---     | :---                                                                                         |
| `virtual_cpu`  | Integer | **Yes**  | The virtual CPU (vCPU) ID of the VNF.                                                        |
| `physical_cpu` | Integer | **Yes**  | The physical CPU thread (logical processor ID) from the hypervisor host to bind the vCPU to. |

### interfaces

| Parameter   | Type   | Required | Description                                                                                                                               |
| :---        | :---   | :---     | :---                                                                                                                                      |
| `name`      | String | **Yes**  | The name of the interface.                                                                                                                |
| `usage`     | String | **Yes**  | The usage type of the interface. Options include `internal`, `out-of-band`, `vlan`, or an interface starting with `hsxe` if using SR-IOV. |
| `mode`      | String | No       | The mode of the interface. **Required if `usage` is set to `vlan`.**                                                                      |
| `vlan_name` | String | No       | The member or VLAN ID name for the interface mapping. TO FIX: Currently only supports one vlan.                                           |

## Dependencies

None.

## Example Playbook

    - hosts: all
      connection: juniper.device.pyez
      gather_facts: false
      roles:
        - iambryant.junos.vnf

## License

MIT
