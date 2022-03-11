* Demo app for Talao wallet 

** Installation 

mkdir delmo
cd demo
python3 -m venv venv
. venv/bin/activate

pip install flask-session
pip install didkit==0.2.1

git clone https://github.com/TalaoDAO/demo

** Run

python issuer.py
python verifier.py

Voir test.py pour des exemples de signature et verifications (doc)

helpers pour des conversions entre ethereum et tezos cle publique/privée et adresses vs JWK