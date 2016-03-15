import java.awt.Color;
import java.util.ArrayList;


public class Frame {
	int width = 600;
	int height = 30;
	int depth = 20;
	int x = 10;
	int y = 10;
	int currentBall = 0;
	private boolean sine;
	
	ArrayList<BallMover> balls = new ArrayList<BallMover>();
	
	boolean allSelected =false;
	
	Renderer render;
	
	public Frame(Renderer r){
		this.render = r;
		
		for (int i=0;i<25;i++){
			balls.add(new BallMover(10,10+i*22,10,10,Color.blue,this,render));
		}
//		for (int i=0;i<10;i++){
//			balls.add(new Ball(10,10+i*22,12,10,Color.blue));
//		}
//		for (int i=0;i<10;i++){
//			balls.add(new Ball(10,10+i*22,14,10,Color.blue));
//		}
		
		balls.get(currentBall).selected = true;
		
	}
	
	public synchronized void selectBall(int i){
		balls.get(currentBall).selected = false;
		currentBall = currentBall+i;
		if(currentBall<0){
			currentBall = balls.size()-1;
		}else if(currentBall>=balls.size()){
			currentBall = 0;
		}
		
		balls.get(currentBall).selected=true;
	}
	
	public synchronized void moveBall(int i){
		if(!allSelected){
			balls.get(currentBall).ball.y_pos+=i;
		}else{
			for(BallMover bm:balls){
				bm.ball.y_pos+=i;
			}
		}
	}
	
	public synchronized void moveCurrentTo(int i){
		balls.get(currentBall).moveTo(i);
		Thread runner = new Thread(balls.get(currentBall));
		runner.start();
	}
	
	public synchronized void sineWave(){
		sine = true;
		Thread runnerSineWave = new Thread(new SineWave(this.render));
		runnerSineWave.start();

	}
	public synchronized void dataModel(){
		sine = false;
		Thread runnerDataModel = new Thread(new DataModel(this.render));
		runnerDataModel.start();

	}
	public synchronized boolean getSine(){
		return sine;
	}
	
	public synchronized void moveBallTo(int i, int y){
		balls.get(i).moveTo(y);
		Thread runner = new Thread(balls.get(i));
		runner.start();
	}
	
	public synchronized void colorBall(Color c){
		balls.get(currentBall).ball.color=c;
	}
	
	public synchronized void toggleAll(){
		allSelected = !allSelected;
	}

}
