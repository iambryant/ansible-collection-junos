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

    acme_key_id: "ACME-KEY"

    acme_certificate_id: "ACME-CERT"

    acme_domain_name: ""

The domain name that will be used for the Let's Encrypt certificate request.

    acme_email: ""

The email to use for Let's Encrypt certificate expiration notices.

    acme_security_zone: "untrust"

The security zone to allow HTTP inbound on. Defaults to `untrust`.

    acme_security_zone_interface: "ge-0/0/0.0"

The interface in the security zone to allow HTTP inbound on. Defaults to `ge-0/0/0.0`.

## Dependencies

None.

## Example Playbook

    - hosts: all
      connection: juniper.device.pyez
      roles:
        - iambryant.junos.acme

## License

MIT
