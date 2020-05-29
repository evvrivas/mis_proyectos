//codio para notificaciones PUSH


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');
//5.4.2

var firebaseConfig = {
    apiKey: "AIzaSyBIYdkebit4PVB6RV2YRSoSgv_da8j8XW8",
    authDomain: "godelivery-c5e59.firebaseapp.com",
    databaseURL: "https://godelivery-c5e59.firebaseio.com",
    projectId: "godelivery-c5e59",
    storageBucket: "godelivery-c5e59.appspot.com",
    messagingSenderId: "873860409720",
    appId: "1:873860409720:web:866cc2fc7321d6df13808d",
    
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  let messaging = firebase.messaging();

  messaging.setBackgroundMessageHandler(function(payload){
  	console.log("LLego notificación");

  	let title = payload.notification.title;
  let options = {
    body: payload.notification.body,
    icon: payload.notification.icon
  }

  self.registration.showNotification(title, options);
  });