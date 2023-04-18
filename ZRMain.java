package main;

public class ZRMain{

    public static void main(String[] args){

        GamePanel gamePanel = new GamePanel();
        GameWindow gameWindow = new GameWindow(gamePanel);
        gamePanel.requestFocus();
    }

}