import sys

domain = sys.argv[1]

print(f'[+] Parameter')
print(f'site:{domain} inurl:= inurl:? inurl:&')
print(f'')

print(f'[+] Program Files')
print(f'site:*.{domain} filetype:sh | filetype:py | filetype:rb')
print(f'')

print(f'[+] Slack Osint')
print(f'site:{domain} "join.slack" ext:pdf "invite"')
print(f'site:{domain} "join.slack" ext:txt | ext:xls | ext:xlsx | ext:zip "invite"')
print(f'site:{domain} "join.slack" ext:pptx | ext:ppt | ext:doc | ext:xml "invite"')
print(f'')

print(f'[+] Sensitive PDF')
print(f'site:{domain} ext:pdf')
print(f'site:{domain} ext:pdf "CONFIDENTIAL"')
print(f'site:{domain} ext:pdf "STRICTLY CONFIDENTIAL"')
print(f'site:{domain} ext:pdf "HIGHLY CONFIDENTIAL"')
print(f'site:{domain} ext:pdf "PRIVATE"')
print(f'site:{domain} ext:pdf "PRIVATE AND CONFIDENTIAL"')
print(f'site:{domain} ext:pdf "PRIVATE AND SENSITIVE"')
print(f'site:{domain} ext:pdf "TRADE SECRET"')
print(f'site:{domain} ext:pdf "NOT FOR DISTRIBUTION"')
print(f'site:{domain} ext:pdf "NOT FOR PUBLIC RELEASE"')
print(f'site:{domain} ext:pdf "EMPLOYEE ONLY"')
print(f'site:{domain} ext:pdf "INTERNAL USE ONLY"')
print(f'site:{domain} ext:pdf "INTERNAL ONLY"')
print(f'')

print(f'[+] Sensitive Documents')
print(f'site:{domain} ext:txt | ext:log | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:sql | ext:git')
print(f'site:{domain} ext:pptx | ext:doc | ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup | ext:zip | ext:config')
print(f'site:{domain} ext:rdp | ext:cfg | ext:ora | ext:ini | ext:env | ext:dbf | ext:mdb | ext:sh | ext:swp | ext:~  ')
print(f'site:{domain} ext:svn | ext:htpasswd | ext:htaccess | ext:json | ext:php | ext:conf | ext:cnf | ext:reg | ext:inf')
print(f'site:{domain} ext:docx intext:"confidential" | intext:"Not for Public Release" | intext:"internal use only" | intext:"do not distribute"')
print(f'site:{domain} intext: "Index of"')
print(f'')

print(f'[+] File Upload')
print(f'site:{domain} intext: Browse | Attach File | Cancel | Upload | Choose File')
print(f'site:{domain} "Choose File"')
print(f'site:{domain} "No file chosen"')
print(f'site:{domain} "Upload"')
print(f'site:{domain} "Upload here"')
print(f'site:{domain} "Upload a file"')
print(f'site:{domain} "Please upload your"')
print(f'')

print(f'[+] WhatsApp Groups OSINT Analysis')
print(f'"KEY WORDS TO FIND" site:chat.whatsapp.com')
print(f'"join whatsapp" | "join my whatsapp"')
print(f'')

print(f'[+] Telegram groups OSINT Analysis')
print(f'"KEY WORDS TO FIND" site:t.me')
print(f'')

print(f'[+] Roxy File Manager Unauth Access')
print(f'site:{domain} intitle:"Roxy file manager"')
print(f'')

print(f'[+] Prometheus Server Unauth Dashboard')
print(f'site:{domain} "Prometheus Time Series Collection and Processing Server" inurl:/alerts')
print(f'site:{domain} "Prometheus Time Series Collection and Processing Server" inurl:/targets')
print(f'')

print(f'[+] SideKiq Instance')
print(f'site:{domain} inurl:/sidekiq intext:"memory usage" intext:"polling interval"')
print(f'')

print(f'[+] X-Prober Server Information Disclosure')
print(f'site:{domain} inurl:/xprober ext:php')
print(f'site:{domain} intitle:xprober intext:CPU')
print(f'')

print(f'[+] Unauth Daskboard via ports')
print(f'site:{domain} inurl:8080/dashboard')
print(f'site:{domain} inurl:8081/dashboard')
print(f'')

print(f'[+] Installation Wizard Unauth Access')
print(f'site:{domain} "iTop Installation Wizard" "Prerequisites validation"')
print(f'')

print(f'[+] UNAUTH SHARE DRIVES')
print(f'site:{domain} "Powered by ZFile"')
print(f'site:{domain} "Powered by FileShelter"')
print(f'site:{domain} "Powered by Izi"')
print(f'site:{domain} "Powered by ShareX Uploader"')
print(f'site:{domain} "Powered by Cloud Commander"')
print(f'site:{domain} "Powered by AList"')
print(f'')


print(f'[+] SharePoint Web Services Exposed Endpoints')
print(f'site:{domain} inurl:_vti_bin inurl:asmx')
print(f'site:{domain} inurl:asmx inurl:services')
print(f'site:{domain} inurl:wsdl inurl:services')
print(f'site:{domain} inurl:wsdl inurl:web')
print(f'site:{domain} inurl:wsdl inurl:server')
print(f'')

print(f'[+] PASTEBIN INFORMATION DISCLOSURE')
print(f'site:pastebin.com "{domain}"')
print(f'')

print(f'[+] PUBLIC CLOUDFLARE R2 BUCKETS')
print(f'site:.r2.dev "{domain}"')
print(f'')

print(f'[+] Symfony Debug Mode Enabled')
print(f'site:{domain} inurl:app_dev.php')
print(f'site:{domain} inurl:app_dev')
print(f'site:{domain} inurl:_profiler')
print(f'site:{domain} inurl:profiler')
print(f'site:{domain} inurl:app_dev.php/_profiler')
print(f'[+] Possible Parameters /app_dev.php/_profiler/open?file=app/config/parameters.yml')
print(f'')

print(f'[+] OAuth Endpoints')
print(f'site:{domain} "Continue with Google"')
print(f'site:{domain} "Sign in with Google"')
print(f'site:{domain} "Login with Google"')
print(f'site:{domain} "Sign in using"')
print(f'site:{domain} "Authenticate with Google"')
print(f'site:{domain} "Authenticate with"')
print(f'[+] https://portswigger.net/web-security/oauth?source=post_page-----134dde35e2d0--------------------------------')
print(f'[+] https://book.hacktricks.xyz/pentesting-web/oauth-to-account-takeover?source=post_page-----134dde35e2d0--------------------------------')
print(f'')

print(f'[+] SWAGGER')
print(f'site:{domain} inurl:swagger')
print(f'')
# https://medium.com/@ghostlulzhacks/swagger-api-c07eca05441e?source=post_page-----134dde35e2d0--------------------------------
# https://blog.vidocsecurity.com/blog/hacking-swagger-ui-from-xss-to-account-takeovers/?source=post_page-----134dde35e2d0--------------------------------
# https://zerotak.com/blog/credentials-harvesting-using-swagger-ui/?source=post_page-----134dde35e2d0--------------------------------
# https://medium.com/@AlQa3Qa3_M0X0101/how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss-e84255eb8c96?source=post_page-----134dde35e2d0--------------------------------

print(f'[+] Old Web Pages')
print(f'site:{domain} ext:old')
print(f'')

print(f'[+] Exposed GRAFANA Dashboard')
print(f'site:{domain} intitle:"Grafana" inurl:"/dashboard/db"')
print(f'')

print(f'[+] Admin Setup')
print(f'site:{domain} "set up the administrator user" inurl:pivot')
print(f'')