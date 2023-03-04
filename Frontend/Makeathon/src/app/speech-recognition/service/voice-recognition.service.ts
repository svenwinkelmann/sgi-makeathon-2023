import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs-compat';


declare var webkitSpeechRecognition: any;

@Injectable({
  providedIn: 'root'
})
export class VoiceRecognitionService {
  private approvalStageMessage = new BehaviorSubject('...');
  currentApprovalStageMessage = this.approvalStageMessage.asObservable();

  recognition = new webkitSpeechRecognition();
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
      console.log('init:' + transcript);
    });
  }

  start() {
    this.text = '';
    this.isStoppedSpeechRecog = false;
    this.recognition.start();
    console.log("Speech recognition started")
    this.recognition.addEventListener('end', (condition) => {
      this.wordConcat()
      this.recognition.stop();
      console.log("End speech recognition");
      this.approvalStageMessage.next(this.text);
    });
  }

  wordConcat() {
    this.text = this.text + ' ' + this.tempWords;
    this.tempWords = '';
  }
}
