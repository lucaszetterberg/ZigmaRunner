package main;

import javax.swing.JFrame;

public class GameWindow {

    public GameWindow(GamePanel gamePanel){
        JFrame window = new JFrame();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setResizable(false);
        window.setTitle("Zigma runner");
        window.setSize(400, 400);
        window.setLocationRelativeTo(null);
        window.add(gamePanel);
        window.setVisible(true);
    }

}
