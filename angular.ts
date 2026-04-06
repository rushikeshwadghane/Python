// Parent HTML

// <h2>Parent Component</h2>

// <p>Message from Child: {{ childResponse }}</p>

// <app-child 
//   [message]="parentMessage" 
//   (reply)="receiveMessage($event)">
// </app-child>

// Parent ts
export class ParentComponent {
  parentMessage = "Hello Child";
  childResponse = "";

  receiveMessage(message: string) {
    this.childResponse = message;
  }

}

// <h3>Child Component</h3>

// <p>Message from Parent: {{ message }}</p>

// <button (click)="sendReply()">Send Reply to Parent</button>

// @Component({
//   selector: 'app-child',
//   templateUrl: './child.component.html'
// })
// export class ChildComponent {

//   @Input() message: string = "";
//   @Output() reply = new EventEmitter<string>();

//   sendReply() {
//     this.reply.emit("Hello Parent");
//   }
// }