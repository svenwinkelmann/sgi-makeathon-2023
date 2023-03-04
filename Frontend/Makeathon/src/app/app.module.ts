import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { Pflanze1Component } from './pflanze1/pflanze1.component';
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
    DialogAnimationsExampleDialog,
    Pflanze1Component
  ],
  imports: [
    BrowserModule,
    MatDialogModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatIconModule
  ],
  providers: [VoiceRecognitionService],
  bootstrap: [AppComponent]
})
export class AppModule { }
