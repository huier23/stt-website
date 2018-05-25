var final_transcript = '';
var recognizing = false;
var showText = document.getElementById('stt_display')
var display = document.getElementById('text_display')
var log = document.getElementById('log')
var record = document.getElementById('rec_button')

if (!('webkitSpeechRecognition' in window)) {
  alert('Your browser is not support this service. Please use Chrome or Opera, else update your browser version.')
} else {
  var recognition = new webkitSpeechRecognition();
  recognition.continuous = false; //辨識一段話完成之後就會結束辨識
  recognition.interimResults=true; //講話當下即時辨識
  recognition.lang="cmn-Hant-TW" //辨識中文

  // execut the function when starting recongnize
  recognition.onstart = function(){
  	recognizing = true;
  	console.log('開始辨識......');
    log.innerHTML = 'Recongnizing Start ...';
  }


  // execut the function when stoping recongnize
  recognition.onend=function(){
  	recognizing = false;
  	console.log('停止辨識!');
    log.innerHTML = 'Recongnizing End !';
    document.getElementById("rec_img").src="/static/image/end.gif";

  }

  recognition.onresult=function(event){
  	var i = event.resultIndex;
  	var j = event.results[i].length-1;
    final_script = event.results[i][j].transcript;
  	showText.innerHTML = final_script;
    console.log(final_script);
    if (event.results[i].isFinal) {
      display.innerHTML += '<p>'+ final_script+'</p>';

    }

    // var final_transcript = '';
    // var interim_transcript = '';
    // for (var i = event.resultIndex; i < event.results.length; ++i) {
    //   if (event.results[i].isFinal) {
    //     final_transcript += event.results[i][0].transcript;
    //   } else {
    //     interim_transcript += event.results[i][0].transcript;
    //   }
    // }
    // final_transcript = capitalize(final_transcript);
    // final_span.innerHTML = linebreak(final_transcript);
    // interim_span.innerHTML = linebreak(interim_transcript);

    // showText.innerHTML += "\n" + final_transcript;


  };
}

function startButton(event){
	if (recognizing) {
      recognition.stop();
      return;
    }
   	recognition.start();

  if (record.onClick && log.value != null){
    log.innerHTML = 'Recongnizing End !';
  }else{
    log.innerHTML = 'Recongnizing Start ...';
    document.getElementById("rec_img").src="/static/image/start.gif";
  }
}



