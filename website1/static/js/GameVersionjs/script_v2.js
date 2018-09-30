$(function () {

try {
  var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recognition = new SpeechRecognition();
  $('#no-browser-support').hide();
}
catch(e) {
  console.error(e);
  $('#no-browser-support').show();
  $('.app').hide();
  $('.headlines').hide();

}


var noteTextarea = $('#note-textarea');
var instructions = $('#recording-instructions');
var notesList = $('ul#notes');

var morehelp = $('#morehelp');
var example = $('#example');
var help = $('.help');

var userID;

var noteContent = '';
var finishFlag=false;
var helpFlag=true;
var RcdingFlag=false;
var counter=0;
var inst = setInterval(change, 1000);



$('#morehelp').hide();
$('#example').hide();
$('#moreExample').hide();
help.hide();
//$('#go-next-btn').hide();
$('#help1').hide();


/*-----------------------------
      variables for game version
------------------------------*/
var answerTime=0;
$('#check1').hide();
$('#check2').hide();
$('#check3').hide();


// Get all notes from previous sessions and display them.
var notes = getAllNotes();
renderNotes(notes);



/*-----------------------------
      Voice Recognition
------------------------------*/

// If false, the recording will stop after a few seconds of silence.
// When true, the silence period is longer (about 15 seconds),
// allowing us to keep recording even when the user pauses.
recognition.continuous = true;

// This block is called every time the Speech APi captures a line.
recognition.onresult = function(event) {

  // event is a SpeechRecognitionEvent object.
  // It holds all the lines we have captured so far.
  // We only need the current one.
  var current = event.resultIndex;

  // Get a transcript of what was said.
  var transcript = event.results[current][0].transcript;

  // Add the current transcript to the contents of our Note.
  // There is a weird bug on mobile, where everything is repeated twice.
  // There is no official solution so far so we have to handle an edge case.
  var mobileRepeatBug = (current == 1 && transcript == event.results[0][0].transcript);

  if(!mobileRepeatBug) {
    noteContent += transcript;
    noteTextarea.val(noteContent);
  }
};

recognition.onstart = function() {
  instructions.text('Voice recognition activated. Try speaking into the microphone.');
}

recognition.onspeechend = function() {
//    if (noteContent.length && !finishFlag) {
//        finishFlag=true;
//        $('#save-note-btn').show();
// //        instructions.text('You were quiet for a while so voice recognition turned itself off. We have got your answer, so you can go next.');
//   }
    //setTimeout("afterEndRcd()",5000)

}

recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    instructions.text('No speech was detected. Try again.');
  };
}




/*-----------------------------
      App buttons and input
------------------------------*/



$('#speak').on('click',function(e){
     if (!RcdingFlag)//start recording
        {
               noteTextarea.val('');
               noteContent = '';
               recognition.start();
               finishFlag=false;
               $('#go-next-btn').hide();
               RcdingFlag=true;
               $("#speak").html('Stop');

               //startRecording();
               startRecordingMp3();
               $('#speak').attr("type","submit");
        }
    else //stop recording
        {
          //afterEndRcd();
              recognition.stop();
              $('#speak').hide();

              instructions.text('Recognizing...Please wait for 2 seconds');
              //stopRecording();
              stopRecordingMp3();
              //afterEndRcd();
              $('#speak').attr("type","button");
              setTimeout(function(){sendfiles()},1500);
               setTimeout(function(){afterEndRcd()},2000);
        }
});


//Sync the text inside the text area with the noteContent variable.
noteTextarea.on('input', function() {
 noteContent = $(this).val();
})




//$('#help-btn').on('click',function(e){
//                  help.toggle();
//                  });






example.on('click',function(e){
           $('#moreExample').show();
           example.hide();
           morehelp.hide();
           });

function change(){ //show up after 5 seconds
    counter++;
    if (counter>1) help.show();
    if (counter>5){
        morehelp.show();
        example.show();
        clearInterval(inst);
    }
};

$('#help-btn').mouseover(function(){
                         $('#help1').show();
                         });
$('#help-btn').mouseout(function(){
                        $('#help1').hide();
                        });

//notesList.on('click', function(e) {
//  e.preventDefault();
//  var target = $(e.target);
//
//  // Listen to the selected note.
//  if(target.hasClass('listen-note')) {
//    var content = target.closest('.note').find('.content').text();
//    readOutLoud(content);
//  }
//
//  // Delete note.
//  if(target.hasClass('delete-note')) {
//    var dateTime = target.siblings('.date').text();
//    deleteNote(dateTime);
//    target.closest('.note').remove();
//  }
//});



/*-----------------------------
      Speech Synthesis
------------------------------*/

//function readOutLoud(message) {
//    var speech = new SpeechSynthesisUtterance();
//
//  // Set the text and voice attributes.
//    speech.text = message;
//    speech.volume = 1;
//    speech.rate = 1;
//    speech.pitch = 1;
//
//    window.speechSynthesis.speak(speech);
//}



/*-----------------------------
      Helper Functions
------------------------------*/


function afterEndRcd(){
  if(!noteContent.length) {
   instructions.text('We could not hear from you. Please try again.');
   $('#speak').html('Speak Again');
   $('#speak').show();
  }
  else{
    if (answerTime >= 2){
      $('#recording-title').hide();
      $('#operation').hide();
     instructions.text('You can go next.');
     finishFlag=true;
     //$('#save-note-btn').show();
     $('#go-next-btn').show();
     $('#check3').show();
     $('#answer3').html('<h5> &nbsp &nbsp  &nbsp  &nbsp 3. &nbsp</h5>')
    }
    else if (answerTime == 0){
      $('#speak').show();
      $('#speak').html('Speak Again');
      instructions.text('Think of another example.');
      answerTime = answerTime+1;
      $('#check1').show();
      $('#answer1').html('<h5> &nbsp &nbsp  &nbsp  &nbsp 1. &nbsp</h5>')
    }
    else{
      $('#speak').show();
      $('#speak').html('Speak Again');
      instructions.text('Think of one last example.');
      answerTime = answerTime+1;
      $('#check2').show();
      $('#answer2').html('<h5> &nbsp &nbsp  &nbsp  &nbsp 2. &nbsp</h5>')
    }

  }
    RcdingFlag=false;
    //$('#speak').html('Speak Again');

    // Save note to localStorage.
    // The key is the dateTime with seconds, the value is the content of the note.
    saveNote(new Date().toLocaleString(), noteContent);

    // Reset variables and update UI.
    noteContent = '';
    renderNotes(getAllNotes());
    noteTextarea.val('');
    finishFlag=false;
    //$('#speak').show();
}

function sendfiles(){
  var formData = new FormData();
  //userID = Cookies.get('userID');
  userID='cat';
  formData.append("queryName", queryName);
  formData.append("text", noteContent);
  formData.append("Mp3url", Mp3url);
  formData.append("userID", userID);
  formData.append("answerTime", answerTime);
  var request = new XMLHttpRequest();
  request.open("POST","/receiveFile_ver_game");
  request.send(formData);
}

//accept notes array and show them on the webpage
function renderNotes(notes) {
  var html = '';
  if(notes.length) {
    notes.forEach(function(note) {
      html+= `<li class="note">
        <p class="header">
          <span class="date">${note.date}</span>

        </p>
        <p class="content">${note.content}</p>
      </li>`;
    });
  }
  else {
    html = '<li><p class="content">You don\'t have any answers yet.</p></li>';
  }
  notesList.html(html);
}


function saveNote(dateTime, content) {
  localStorage.setItem('note-' + dateTime, content);
    // send to flask server
    // send post request
}


//Get notes from localStorage, return them as an array
function getAllNotes() {
  var notes = [];
  var key;
  for (var i = 0; i < localStorage.length; i++) {
    key = localStorage.key(i);

    if(key.substring(0,5) == 'note-') {
      notes.push({
        date: key.replace('note-',''),
        content: localStorage.getItem(localStorage.key(i))
      });
    }
  }
  return notes;
}




//function deleteNote(dateTime) {
//  localStorage.removeItem('note-' + dateTime);
//}

  });
