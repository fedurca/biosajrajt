#/bin/bash
curl -o cepro_data.json -0 -v -X POST https://einfo.ceproas.cz/cepro_portal_ws/rest/common/prox/mobileData \
-H 'accept-encoding: gzip' \
-H 'authorization: Basic bW9iYXA6RVdpa0Ey' \
-H 'connection: Keep-Alive' \
-H 'content-length: 99' \
-H 'content-type: application/json; charset=UTF-8' \
-H 'host: einfo.ceproas.cz' \
-H 'user-agent: okhttp/4.9.0' \
--data-binary @- << EOF
{
  "search": {
    "exclude_cs_ceny": false,
    "exclude_cs_kvalita": false
  },
  "version": 5
}
EOF
