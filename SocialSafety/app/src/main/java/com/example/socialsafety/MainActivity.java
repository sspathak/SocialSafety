package com.example.socialsafety;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.TextView;
import android.widget.ToggleButton;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    BluetoothAdapter mBluetoothAdapter;
    public ArrayList<BluetoothDevice> list;
    StringBuilder names = new StringBuilder();
    StringBuilder mac_add = new StringBuilder();
    int count = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button toggleBtn = (Button) findViewById(R.id.buttonToggle);
        ToggleButton scan = (ToggleButton) findViewById((R.id.scanBtn));
        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        list = new ArrayList<BluetoothDevice>();


        scan.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                checkPerm();
                Log.d("Manifest", "ClickedToggle");
                IntentFilter filter = new IntentFilter(BluetoothDevice.ACTION_FOUND);
                if(isChecked){
                    registerReceiver(bReciever, filter);
                    mBluetoothAdapter.startDiscovery();
                }
                else{
                    unregisterReceiver(bReciever);
                    mBluetoothAdapter.cancelDiscovery();
                    names = new StringBuilder();
                    mac_add = new StringBuilder();
                }
            }
        });



        toggleBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                enableDisableBT();
                Log.d("Z","BT ON");
            }
        });




    }


    private final BroadcastReceiver bReciever = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (BluetoothDevice.ACTION_FOUND.equals(action)) {
                BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                // Create a new device item
//                DeviceItem newDevice = new DeviceItem(device.getName(), device.getAddress(), "false");
                // Add it to our adapter
//                mAdapter.add(newDevice);
                if(device.getName() == null){
                    mac_add.append("Masked Device :"+device.getAddress()+"\n");
                }
                else {
                    mac_add.append(device.getName()+" : "+device.getAddress()+"\n");
                }
                count+=1;
                goPrint();
                Log.d("BTBTBTBTB", "FOUND SOMETHING"+ device.getName());
            }
        }
    };
    public void goPrint(){
        TextView addView = (TextView) findViewById(R.id.device_mac);
        TextView countV = (TextView) findViewById(R.id.countView);
        TextView overAllScore = (TextView) findViewById(R.id.textView);
        Log.d("X", "s"+count);
        overAllScore.setText(100 - count+"");
        addView.setText(mac_add);
        countV.setText(count+"");

    }

    public void enableDisableBT(){
        if(mBluetoothAdapter == null){
            Log.d("Not working", "BT not supported");
        }
        if(!mBluetoothAdapter.isEnabled()) {
            Intent enable = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
//            enable.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 3600);
            startActivity(enable);
        }
        if(mBluetoothAdapter.isEnabled()){
            mBluetoothAdapter.disable();
        }
    }

     public void checkPerm(){
        int MY_PERMISSIONS_REQUEST_ACCESS_COARSE_LOCATION = 1;
        ActivityCompat.requestPermissions(this,
                new String[]{Manifest.permission.ACCESS_COARSE_LOCATION},
                MY_PERMISSIONS_REQUEST_ACCESS_COARSE_LOCATION);
    }

}
