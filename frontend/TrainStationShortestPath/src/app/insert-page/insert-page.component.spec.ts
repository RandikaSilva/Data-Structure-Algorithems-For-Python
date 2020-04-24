import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InsertPageComponent } from './insert-page.component';

describe('InsertPageComponent', () => {
  let component: InsertPageComponent;
  let fixture: ComponentFixture<InsertPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InsertPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InsertPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
