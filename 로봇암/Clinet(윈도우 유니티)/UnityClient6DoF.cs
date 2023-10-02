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
        client = new TcpClient("165.194.69.75", 12345);
        stream = client.GetStream();

        initialPosition = transform.position;
        initialRotation = transform.rotation.eulerAngles;
    }

    void Update()
    {
        if (stream.DataAvailable)
        {
            byte[] data = new byte[client.ReceiveBufferSize];
            int bytesRead = stream.Read(data, 0, client.ReceiveBufferSize);
            string message = encoder.GetString(data, 0, bytesRead);

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
                x = initialPosition.x+(x / 100.0f) +4 ;
                y = initialPosition.y+(y / 100.0f) +3 ;
                z = initialPosition.z+(z / 100.0f);
                roll = initialRotation.x + (roll / 100.0f) + 10 ;
                pitch = initialRotation.y + pitch ;
                yaw = initialRotation.z + (yaw / 100.0f)  ;
                // Update the camera's position and rotation
                transform.position = new Vector3(-y, x, z);
                transform.eulerAngles = new Vector3(roll, pitch, yaw); //-yaw, roll, pitch
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
