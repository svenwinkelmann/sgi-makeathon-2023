import { Component, OnInit } from '@angular/core';
import { VoiceRecognitionService } from '../service/voice-recognition.service';

@Component({
  selector: 'app-speech-to-text',
  templateUrl: './speech-to-text.component.html',
  styleUrls: ['./speech-to-text.component.css']
})
export class SpeechToTextComponent implements OnInit {


  constructor(
    public service : VoiceRecognitionService
  ) { 
    this.service.init()
   }

  ngOnInit(): void {
  }

  startService() {
    this.service.start().subscribe(text => {
      this.startHttpRequest(text);
    })
  }

  startHttpRequest(text: string){
    if(text === "how is my plant"){
      console.log("Request an Backend");
    }
    else if(text === "how is my plant Berta"){
      console.log("Request an Backend");
    }
    else if(text === "okay"){
      console.log("Request an Backend");
    }
    else if(text === ""){
      console.log("START wurde übergeben");
    }
    else{
      console.log("TEXT ist scheiße");
    }
  }


  // stopService(){
  //   this.service.stop()
  // }

}