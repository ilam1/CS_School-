//Irene Lam
//APCS1 pd5
//HW08 - On the Origins of a BigSib/ Adding two constructors
//2016-09-25

public class BigSib {
    private String helloMsg;
    public void setHelloMsg(String name) {
	helloMsg = name;
    }
    public BigSib(String Name) {
       	helloMsg = Name;
    }
    public BigSib() {
       	helloMsg = "";
    }

    public String getHelloMsg(){
	return helloMsg;
    }

    public String greet(String name){
	helloMsg = helloMsg + " " + name;
	return helloMsg;
    }
    //    public BigSib( String newMsg ) {
    //	helloMsg = newMsg;
    // public String greet(String name) {
    //	return helloMsg + " " + name;
    // }
    
}
