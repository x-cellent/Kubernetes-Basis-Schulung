Erstellen Sie einen zweiten Container für den nginx webserver.
Dieser soll in die Webseite des nginx alle 5 Sekunden eine Zeile schreiben.
Das Command dafür kann z.B. folgendermaßen aussehen:
```
command: ["/bin/sh"]
args: ["-c", "while true; do echo $(date -u) 'Hi I am from Sidecar container' >> /var/log/index.html; sleep 5; done"]
```

