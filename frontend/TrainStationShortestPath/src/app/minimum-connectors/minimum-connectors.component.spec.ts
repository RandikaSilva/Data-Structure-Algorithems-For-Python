import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MinimumConnectorsComponent } from './minimum-connectors.component';

describe('MinimumConnectorsComponent', () => {
  let component: MinimumConnectorsComponent;
  let fixture: ComponentFixture<MinimumConnectorsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MinimumConnectorsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MinimumConnectorsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
