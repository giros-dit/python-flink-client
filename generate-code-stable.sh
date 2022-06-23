docker run --rm  -u `id -u`:`id -g` \
    -v ${PWD}:/local openapitools/openapi-generator-cli:v6.0.0 generate \
    -i /local/specs/rest_v1_dispatcher.yml \
    -g python \
    -o /local/ --global-property skipFormModel=false \
    --package-name flink_client


