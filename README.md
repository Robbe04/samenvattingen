Deze Repository bevat alle samenvattingen van _Toegepaste Informatica_ 

De samenvattingen worden elk weekend geüpdatet (zaterdag- of zondagavond)  

 **Jaar 1 - Semsester 1**  
 - Web Development,  
 - Object Oriënted Software Development I,   
 - IT-Fundamentals,   
 - Computers Systems,   
 - Databases,   
 - Cybersecurity,   
 - Software Analasis
    
 **Jaar 1 - Semsester 2**  
 - Web Development II,   
 - Object Oriënted Software Development II,   
 - Communication Lab,   
 - Computers Networks I,   
 - Business & Management,   
 - Operating Systems   

// wachtwoord ophalen via hydra
`cd Documents; hydra -l osboxes -P wordlist.txt ssh://192.168.56.20 - V`

// whitelisten IP indien gebanned
`sudo fail2ban-client set sshd unbanip 192.168.56.20 || sudo fail2ban-client set ssdh unbanip 192.168.56.20`

    
