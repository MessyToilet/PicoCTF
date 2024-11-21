1. find correct file from files/, 

sha256sum files/*

2. find correct has from files (file that matches checksum), 

sha256sum files/* | grep b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2

3. run the decrypt scrip on file

./decrypt.sh files/451fd69b
 
 Flag: picoCTF{trust_but_verify_451fd69b}

