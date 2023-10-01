using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class UnityClient6DoF : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private ASCIIEncoding encoder = new ASCIIEncoding();

    void Start()
    {
        client = new TcpClient("192.168.1.196", 12345);
        stream = client.GetStream();
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

                // Update the camera's position and rotation
                transform.position = new Vector3(x, y, z);
                transform.eulerAngles = new Vector3(roll, pitch, yaw);
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
