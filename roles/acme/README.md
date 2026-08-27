# Ansible Role: ACME

This role configures ACME on Junos OS as per Juniper's [documentation](https://www.juniper.net/documentation/us/en/software/junos/pki/topics/topic-map/enroll-certificates.html#id_ikf_m2t_lfc).

## Requirements

Check [here](https://apps.juniper.net/feature-explorer/feature/7429?fn=Automated%20Certificate%20Management%20Environment%20(ACME)%20protocol)
for supported SRX model and Junos OS release combinations.

## Role Variables

    acme_ca_profile_name: "Lets_Encrypt"

    acme_ca_identity: "Lets_Encrypt"

    acme_url: "https://acme-v02.api.letsencrypt.org/directory"

The API endpoint to use for certificate requests. Defaults to `https://acme-v02.api.letsencrypt.org/directory`.

    acme_key_type: "ecdsa"

    acme_key_size: "256"

The key type and size to use for generating key-pairs. Defaults to key type `ecdsa` with a key size of `256`.

    acme_key_id: "ACME-ACCOUNT-KEY"

The name to use for the key-pair generated to talk to Let's Encrypt. Defaults to `ACME-ACCOUNT-KEY`.

    acme_domain_names: []

The domain names that will be used for Let's Encrypt certificate requests.

    acme_email: ""

The email to use for Let's Encrypt certificate expiration notices.

    acme_security_zone: "untrust"

The security zone to allow HTTP inbound on. Defaults to `untrust`.

    acme_security_zone_interface: "ge-0/0/0.0"

The interface in the security zone to allow HTTP inbound on. Defaults to `ge-0/0/0.0`.

    acme_timeout: 30

The maximum number of seconds to wait for the Let's Encrypt certificate request to be processed. Defaults to `30`.

## Dependencies

None.

## Example Playbook

    - hosts: all
      connection: juniper.device.pyez
      gather_facts: false
      roles:
        - iambryant.junos.acme

## License

MIT
