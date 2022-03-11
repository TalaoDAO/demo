

import json
from flask import Flask, jsonify
from flask_session import Session


# Server Release
VERSION = '0.1'


# Framework Flask and Session setup
app = Flask(__name__)
sess = Session()

"""
# Google universal link
@app.route('/.well-known/assetlinks.json' , methods=['GET']) 
def assetlinks(): 
    document = json.load(open('assetlinks.json', 'r'))
    return jsonify(document)


# Apple universal link
@app.route('/.well-known/apple-app-site-association' , methods=['GET']) 
def apple_app_site_association(): 
    document = json.load(open('apple-app-site-association', 'r'))
    return jsonify(document)
"""


# .well-known DID API DID document
@app.route('/', methods=['GET'])
def start():
    return jsonify('Everything is fine')


# .well-known DID API DID document
@app.route('/.well-known/did.json', methods=['GET'])
def well_known_did () :
    """ did:web
    https://w3c-ccg.github.io/did-method-web/
    https://identity.foundation/.well-known/resources/did-configuration/#LinkedDomains
    """
    return  {
                "@context": [
                    "https://www.w3.org/ns/did/v1",
                    {
                        "@id": "https://w3id.org/security#publicKeyJwk",
                        "@type": "@json"
                    }
                ],
                "id": "did:web:demo.talao.co",
                "verificationMethod": [
                    
                    {
                        "id": "did:web:demo.talao.co#key-1",
                        "type": "JwsVerificationKey2020",
                        "controller": "did:web:demo.talao.co",
                        "publicKeyJwk": {
                            "e":"AQAB",
                            "kid":"did:web:demo.talao.co#key-1",
                            "kty":"RSA",
                            "n": "ilResnUjv6kwJW8yh9u3kS3_2hWYtHD-hN0tBUaSe6UdhGYvmLUxRzyssEs5ib_JjChyhrvFbgWpSmRQK5wQEgGnhxs1isdXXNsEIQY0hKxwR1s5b2WxHsGi65bYMOFr_s2ZkNTpWDnlGNjpvw16Cnp94Ak9GUSHMf1HzQP2C5ou6l6k9Iz4CHpYZCPuM5kaerFDfN-TyQRVnek6vN7rFXbtgaBGzwDVl1aQa75jd5osmMy_43brnQsl2bFwoJLxzzye9V-nBKqZWsMi2V6tB_loYUhBTtxlKyY53R9QoNtJTwx25KMjHIpDCrPoSDXyYV_JfjW9iNGZenNbpoLS6Q"
                        }
                    },
                ],
                "authentication" : [
                    "did:web:demo.talao.co#key-1",
                ],
                "assertionMethod" : [
                    "did:web:demo.talao.co#key-1",
                ],
                "capabilityInvocation":[
                    "did:web:demo.talao.co#key-1"
                ]
            }



# MAIN entry point for test
if __name__ == '__main__':
    # info release
    app.run(host = "127.0.0.1", port= 5000, debug=True)