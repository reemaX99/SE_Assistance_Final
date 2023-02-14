class InteractiveChatbox {
    constructor(a, b, c ,d) {
        this.args = {
            button: a,
            chatbox: b,
            SendButton: c
        }
        this.icons = d;
        this.state = false;
        this.messages=[];
    }

  display() {
      const {button, chatbox,SendButton} = this.args;

      button.addEventListener('click', () => this.toggleState(chatbox));
      SendButton.addEventListener('click', () => this.onSendButton());

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup" , ({key}) => {
           if(key == "Enter"){
          this.onSendButton(chatBox);
         }});


  }

    toggleState(chatbox) {
        this.state = !this.state;
        this.showOrHideChatBox(chatbox, this.args.button);
    }

    showOrHideChatBox(chatbox, button) {
        if(this.state) {
            chatbox.classList.add('chatbox--active')
            this.toggleIcon(true, button);
        } else if (!this.state) {
            chatbox.classList.remove('chatbox--active')
            this.toggleIcon(false, button);
        }
    }

    toggleIcon(state, button) {
        const { isClicked, isNotClicked } = this.icons;
        let b = button.children[0].innerHTML;

        if(state) {
            button.children[0].innerHTML = isClicked;
        } else if(!state) {
            button.children[0].innerHTML = isNotClicked;
        }
    }

    onSendButton(){
       var textField = document.querySelector('.msq_content');
       let text1=textField.value
       if(text1 === ""){
         return;
       }
       let msg1 ={name:"User",message :text1}
       this.messages.push(msg1)

       fetch('http://127.0.0.1:8000/predict',{
        method:'POST',
        data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
        body:JSON.stringify({message:text1}),
        mode:'cors',
        headers:{
          'Content-Type': 'application/json'
        },
       })
       .then(r => r.json())
       .then(r=>{
         let msg2 ={name:"Sam" , message: r.answer};
         this.messages.push(msg2);
         this.updateChatText();
         textField.value='';

       }).catch((error) => {
          console.error('Error:',error);
          this.updateChatText();
          textField.value='';
       });
     }

     updateChatText(){
     var html ='';
     this.messages.slice().reverse().forEach(function(item,index){
       if(item.name ==="Sam"){
         html += '<div class ="messages__item messages__item--visitor">' + item.message+'</div>'
       }
       else{
         html += '<div class ="messages__item messages__item--operator">' + item.message +'</div>'
       }
     });

     const chatmessage = document.querySelector('.chatbox__messages');
     chatmessage.innerHTML =html ;


     }
}
const chatButton = document.querySelector('.chatbox__button');
const chatContent = document.querySelector('.chatbox__support');
const SendButton = document.querySelector('.chatbox__send');

const icons = {
    isClicked: '<img src="/static/img/chatbox-icon.svg" />',
    isNotClicked: '<img src="/static/img/chatbox-icon.svg" />'
}
const chatbox = new InteractiveChatbox(chatButton, chatContent,SendButton,icons );
chatbox.display();
chatbox.toggleIcon(false, chatButton);
