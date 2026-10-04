// Existe só para o navegador oferecer "Instalar app" (o botão Baixar).
// Não guarda cópia de nada: cópia velha de página é o que faz app instalado
// mostrar tela antiga depois de uma atualização. Os dados no celular quem
// guarda é o Firestore.
self.addEventListener("install", function(){ self.skipWaiting(); });
self.addEventListener("activate", function(e){ e.waitUntil(self.clients.claim()); });
self.addEventListener("fetch", function(e){ e.respondWith(fetch(e.request)); });
