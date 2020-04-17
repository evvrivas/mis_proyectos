//codio para notificaciones PUSH


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');
//5.4.2

var firebaseConfig = {
    apiKey: "AIzaSyD4FDKeln63jm4VnY3D6AOUuO-q89QHX48",
    authDomain: "detodonegocio-dbc1e.firebaseapp.com",
    databaseURL: "https://detodonegocio-dbc1e.firebaseio.com",
    projectId: "detodonegocio-dbc1e",
    storageBucket: "detodonegocio-dbc1e.appspot.com",
    messagingSenderId: "152761675312",
    appId: "1:152761675312:web:b91be95a396f1e8d4387f5",
    
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  let messaging = firebase.messaging();

  messaging.setBackgroundMessageHandler(function(payload){
  	console.log("ha lleado notificacion");

  	let title = payload.notification.title;
  let options = {
    body: payload.notification.body,
    icon: payload.notification.icon
  }

  self.registration.showNotification(title, options);
  });