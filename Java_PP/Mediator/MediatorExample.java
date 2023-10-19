package Java_PP.Mediator;

import java.util.ArrayList;
import java.util.List;

// Mediator
class ChatMediator {
    private List<ChatUser> users = new ArrayList<>();

    public void addUser(ChatUser user) {
        users.add(user);
    }

    public void sendMessage(String message, ChatUser sender) {
        for (ChatUser user : users) {
            if (user != sender) {
                user.receive(message);
            }
        }
    }
}

// Colleague
class ChatUser {
    private String name;
    private ChatMediator mediator;

    public ChatUser(String name, ChatMediator mediator) {
        this.name = name;
        this.mediator = mediator;
    }

    public void send(String message) {
        System.out.println(name + " sends: " + message);
        mediator.sendMessage(message, this);
    }

    public void receive(String message) {
        System.out.println(name + " received: " + message);
    }
}

public class MediatorExample {
    public static void main(String[] args) {
        ChatMediator chatMediator = new ChatMediator();

        ChatUser user1 = new ChatUser("Alice", chatMediator);
        ChatUser user2 = new ChatUser("Bob", chatMediator);
        ChatUser user3 = new ChatUser("Charlie", chatMediator);

        chatMediator.addUser(user1);
        chatMediator.addUser(user2);
        chatMediator.addUser(user3);

        user1.send("Hello, everyone!");
    }
}
