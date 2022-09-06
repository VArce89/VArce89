apt-get install stunnel4 -y
echo -e "client = no
[SSL]
cert = /etc/stunnel/stunnel.pem
accept = 443 
connect = 127.0.0.1:80" > /etc/stunnel/stunnel.conf
openssl genrsa -out stunnel.key 2048 > /dev/null 2>&1
(echo "" ; echo "" ; echo "" ; echo "" ; echo "" ; echo "" ; echo "@cloudflare" )|openssl req -new -key stunnel.key -x509 -days 1000 -out stunnel.crt 
cat stunnel.crt stunnel.key > stunnel.pem 
mv stunnel.pem /etc/stunnel/
sed -i 's/ENABLED=0/ENABLED=1/g' /etc/default/stunnel4
service stunnel4 restart 
rm -rf /etc/ger-frm/stunnel.crt 
rm -rf /etc/ger-frm/stunnel.key
rm -rf /root/stunnel.crt
rm -rf /root/stunnel.key
