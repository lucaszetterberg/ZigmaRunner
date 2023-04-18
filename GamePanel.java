package main;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;
import inputs.KeyboardInputs;

public class GamePanel extends JPanel{

    private int xDelta = 0;
    private int yDelta = 0;
    
    public GamePanel(){
        addKeyListener(new KeyboardInputs(this));
    }

    public void changeXDelta(int increment){
        this.xDelta += increment;
        repaint();
    }

    public void changeYDelta(int increment){
        this.yDelta += increment;
        repaint();
    }

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.fillRect(100 + xDelta, 100 + yDelta, 200, 50);
    }
}