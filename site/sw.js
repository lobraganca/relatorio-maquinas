// Existe para o navegador oferecer "Instalar app" (o botão Baixar) e para
// o app sempre abrir a versão mais nova.
//
// A página é sempre buscada de novo no servidor (cache: "no-store"): o
// GitHub Pages manda guardar por 10 minutos, e o app instalado no celular
// chegava a mostrar a versão anterior depois de uma mudança — a dona viu
// "caminhões paradas" depois de já estar "parados" no ar.
// Nada é guardado aqui; os dados no celular quem guarda é o Firestore.
self.addEventListener("install", function(){ self.skipWaiting(); });
self.addEventListener("activate", function(e){ e.waitUntil(self.clients.claim()); });
self.addEventListener("fetch", function(e){
  if (e.request.mode === "navigate") {
    e.respondWith(fetch(e.request, {cache: "no-store"}).catch(function(){ return fetch(e.request); }));
    return;
  }
  e.respondWith(fetch(e.request));
});
