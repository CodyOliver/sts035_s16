import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;


public class Renderer extends JPanel {

	String filename;

	private ArrayList<String> nodes;
	private ArrayList<String> path;
	
	Frame artFrame = new Frame(this);


	public Renderer() {
		

	}


	//repaint method for Java swing functionality
	@Override
	public void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;
		
		g2.setColor(Color.GRAY);
		g2.setStroke(new BasicStroke(3.0f));
		g2.fillRect(artFrame.x,artFrame.y, artFrame.width, artFrame.height);
		
		int x_offset = artFrame.x;
		int y_offset = artFrame.y+artFrame.height;
		
		for(BallMover bm:artFrame.balls){
			Ball b = bm.ball;
			g2.setColor(b.color);
			if(bm.selected){
				g2.setColor(Color.cyan);
			}
			if(artFrame.allSelected){
				g2.setColor(Color.cyan);
			}
			g2.fillOval(b.x_pos+x_offset, b.y_pos+y_offset,b.diameter, b.diameter);
		
			g2.setStroke(new BasicStroke(1.0f));
			g2.setColor(Color.LIGHT_GRAY);
			g2.drawLine(x_offset+b.x_pos+b.diameter/2, y_offset, b.x_pos+x_offset+b.diameter/2, b.y_pos+y_offset);

		}

	}
	
	public void addTouch(JFrame frame,Renderer render){
		
		frame.addKeyListener(new KeyListener() {
            public void keyReleased(KeyEvent e) {
            	int key=e.getKeyCode();
                if(key==KeyEvent.VK_ESCAPE){  
                	System.exit(0);
                	System.out.println("pressed escape");
                    }
            }
 
            public void keyTyped(KeyEvent e) {

            }
 
            public void keyPressed(KeyEvent e) {
            	
            	int key=e.getKeyCode();

//            	if(key==KeyEvent.VK_S){
//                	if(multiplayer){
//                		client.sendInitialization();
//                	}
//            	}
            	if(key==KeyEvent.VK_K){
            		render.artFrame.colorBall(Color.black);
            	}
            	if(key==KeyEvent.VK_B){
            		render.artFrame.colorBall(Color.blue);
            	}
            	if(key==KeyEvent.VK_R){
            		render.artFrame.colorBall(Color.red);
            	}
            	if(key==KeyEvent.VK_G){
            		render.artFrame.colorBall(Color.green);
                       		
            	}
            	
            	if(key==KeyEvent.VK_0){
            		render.artFrame.moveCurrentTo(10);
            	}
            	if(key==KeyEvent.VK_1){
            		render.artFrame.moveCurrentTo(30);
            	}
            	if(key==KeyEvent.VK_2){
            		render.artFrame.moveCurrentTo(50);
            	}
            	if(key==KeyEvent.VK_3){
            		render.artFrame.moveCurrentTo(70);
            	}
            	if(key==KeyEvent.VK_4){
            		render.artFrame.moveCurrentTo(90);
            	}
            	if(key==KeyEvent.VK_5){
            		render.artFrame.moveCurrentTo(110);
            	}
            	
            	if(key==KeyEvent.VK_S){
            		render.artFrame.sineWave();
            	}
            	
            	if(key==KeyEvent.VK_T){
            		render.artFrame.dataModel();
            	}
            	
            	
            	if(key==KeyEvent.VK_A){
            		render.artFrame.toggleAll();
            	}
//            	
//            	if(key==KeyEvent.VK_P){
//            		MusicPlayer music = new MusicPlayer();
//            		music.playSound("FFMusictest.wav");
//            	}
//            	
//            	if(key==KeyEvent.VK_1){
//            		System.out.println("1");
//            		currentUnit = canvas.updateCurrentUnit(1);
//            	}
//            	if(key==KeyEvent.VK_2){
//            		System.out.println("2");
//            		currentUnit = canvas.updateCurrentUnit(2);
//            	}
//            	if(key==KeyEvent.VK_3){
//            		currentUnit = canvas.updateCurrentUnit(3);
//            	}
//            	
//            	if(!waitMode){
//            	
//            	if(key==KeyEvent.VK_ENTER){
//            		if(host){
//            			computerTurns();
//            		}
//            		else{
//            			switchTurns();
//            		}
//            		
//            	}
//            	
                if(key==KeyEvent.VK_DOWN){
                	render.artFrame.moveBall(10);}	
                
                if(key==KeyEvent.VK_UP){
                	render.artFrame.moveBall(-10);}
            
                if(key==KeyEvent.VK_LEFT){
                	render.artFrame.selectBall(-1);
                	System.out.println("hit left");
                    }	

                if(key==KeyEvent.VK_RIGHT){
                	render.artFrame.selectBall(1);
                	System.out.println("hit right");	
            	}
            
                render.repaint();
            }
            
		});
	}


	public void showGUI() {
//      //Create and set up the window.
      JFrame frame = new JFrame("Kinetic Sculpture");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

//      //add the graph printout text
      addTouch(frame,this);
      this.repaint();
      frame.add(this);

      frame.pack();
      frame.setSize(700, 700);
      frame.setLocation(500,100);
      frame.setVisible(true);
  }
	
	public void playAnim1(){
		
	}
	
	
}
