using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class UnityClient6DoF : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private ASCIIEncoding encoder = new ASCIIEncoding();

    private Vector3 initialPosition;  // 초기 위치를 저장할 변수
    private Vector3 initialRotation;  // 초기 회전값을 저장할 변수

    void Start()
    {
        client = new TcpClient("165.194.69.79", 12345);
        stream = client.GetStream();

        initialPosition = transform.position;
        initialRotation = transform.rotation.eulerAngles;

        //transform.position = new Vector3(-3.0f, 0.0f, -3.0f);
        //transform.eulerAngles = new Vector3(5.0f, 15.0f, 0.0f); //-yaw, roll, pitch
    }

    void Update()
    {
        if (stream.DataAvailable)
        {
            byte[] data = new byte[client.ReceiveBufferSize];
            int bytesRead = stream.Read(data, 0, client.ReceiveBufferSize);
            string message = encoder.GetString(data, 0, bytesRead);
            float initx = 0;
            float inity = 0;
            float initz = 4;
            float initRx = 0;
            float initRy = 180;
            float initRz = 0;
            // Parse the 6 DOF values from the message
            string[] coordinates = message.Split(',');
            if (coordinates.Length == 6)
            {
                float x = float.Parse(coordinates[0].Trim());
                float y = float.Parse(coordinates[1].Trim());
                float z = float.Parse(coordinates[2].Trim());
                float roll = float.Parse(coordinates[3].Trim());
                float pitch = float.Parse(coordinates[4].Trim());
                float yaw = float.Parse(coordinates[5].Trim());
                x =  (x / 100.0f);
                y =  (y / 100.0f);
                z =  (z / 100.0f);
                roll = roll;
                pitch =  pitch;
                yaw =  yaw;
                // Update the camera's position and rotation
                transform.position = new Vector3(initx+y, inity+z , initz-x );
                transform.eulerAngles = new Vector3(initRx -roll, initRy-yaw  , initRz-pitch); //-yaw, roll, pitch //(initRx + roll , initRy + yaw , initRz+ pitch);
            }
            else if (message == "MOVE_RIGHT")
            {
                transform.Translate(Vector3.right * Time.deltaTime);
                Debug.Log("MOVE_RIGHT");
            }
            else if (message == "MOVE_LEFT")
            {
                transform.Translate(Vector3.left * Time.deltaTime);
                Debug.Log("MOVE_LEFT");
            }
            // ... handle other messages
        }

    }

    void OnApplicationQuit()
    {
        if (client != null)
        {
            client.Close();
        }
    }
}