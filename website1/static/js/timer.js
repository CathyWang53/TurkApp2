$(function () {
  var sec = Number(Cookies.get('timer'));
  setInterval(function(){
    sec=sec+1;
    Cookies.set('timer', sec.toString());
  },1000);
});
