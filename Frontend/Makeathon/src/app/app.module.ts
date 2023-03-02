import { NgModule } from '@angular/core';
import { MatDialogModule } from '@angular/material/dialog';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { DialogAnimationsExampleDialog, PopUpComponent } from './pop-up/pop-up.component';
import { VoiceRecognitionService } from './speech-recognition/service/voice-recognition.service';
import { SpeechRecognitionComponent } from './speech-recognition/speech-recognition.component';
import { SpeechToTextComponent } from './speech-recognition/speech-to-text/speech-to-text.component';

@NgModule({
  declarations: [
    AppComponent,
    PopUpComponent,
    SpeechRecognitionComponent,
    SpeechToTextComponent,
    DialogAnimationsExampleDialog
  ],
  imports: [
    BrowserModule,
    MatDialogModule,
    BrowserAnimationsModule
  ],
  providers: [VoiceRecognitionService],
  bootstrap: [AppComponent]
})
export class AppModule { }
