import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Pflanze1Component } from './pflanze1.component';

describe('Pflanze1Component', () => {
  let component: Pflanze1Component;
  let fixture: ComponentFixture<Pflanze1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Pflanze1Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Pflanze1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
