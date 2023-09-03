public class MyVector3D {
    float x, y, z, w = 1;

    public MyVector3D(float x, float y, float z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public MyVector3D(float x, float y, float z, float w){
        this.x = x;
        this.y = y;
        this.z = z;
        this.w = w;
    }

    public MyVector3D(){
        this.x = 0.0f;
        this.y = 0.0f;
        this.z = 0.0f;
        this.w = 1.0f;
    }
}
