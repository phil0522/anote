cd $(dirname "${0}")
protoc anote.proto --python_out=../../anote-web/anoteweb/data/
cd -
