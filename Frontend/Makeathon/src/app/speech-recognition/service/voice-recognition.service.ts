import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { of } from 'rxjs/internal/observable/of';


declare var webkitSpeechRecognition: any;

@Injectable({
  providedIn: 'root'
})
export class VoiceRecognitionService {

 recognition =  new webkitSpeechRecognition();
  isStoppedSpeechRecog = false;
  public text = '';
  tempWords;

  constructor() { }

  init() {

    this.recognition.interimResults = true;
    this.recognition.lang = 'en-US';

    this.recognition.addEventListener('result', (e) => {
      const transcript = Array.from(e.results)
        .map((result) => result[0])
        .map((result) => result.transcript)
        .join('');
      this.tempWords = transcript;
      console.log(transcript);
    });
  }

  start(): Observable<string>{
    this.text = '';
    this.isStoppedSpeechRecog = false;
    this.recognition.start();
    console.log("Speech recognition started")
    this.recognition.addEventListener('end', (condition) => {
      // if (this.isStoppedSpeechRecog) {
      //   this.recognition.stop();
      //   console.log("End speech recognition")
      // } else {
      //   this.wordConcat()
      //   this.recognition.start();
      // }
      this.wordConcat()
      this.recognition.stop();
      console.log("End speech recognition");

    });
    
    return of(this.text);
  }
  // stop() {
  //   this.isStoppedSpeechRecog = true;
  //   this.wordConcat()
  //   this.recognition.stop();
  //   console.log("End speech recognition")
  // }

  wordConcat() {
    this.text = this.text + ' ' + this.tempWords;
    this.tempWords = '';
  }
}
