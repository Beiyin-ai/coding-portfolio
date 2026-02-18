package com.example.myapplication_0920

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myapplication_0920.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity(), SampleItemAdapter.OnItemClickListener {


    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val items = generateFakeData(100)

        val recyclerView = binding.recyclerView
        recyclerView.layoutManager = GridLayoutManager(this, 2)
        // recyclerView.layoutManager = LinearLayoutManager(this)

        val adapter = SampleItemAdapter(items)
        adapter.setOnItemClickListener(this)

        recyclerView.adapter = adapter

        recyclerView.addItemDecoration(
            DividerItemDecoration(
                this@MainActivity,
                DividerItemDecoration.VERTICAL
            )
        )

    }

    private fun generateFakeData(count: Int): List<SampleItem> {
        val fakeData = mutableListOf<SampleItem>()
        for (i in 1..count) {
            fakeData.add(SampleItem("Item $i", "This is Description $i"))
        }
        return fakeData
    }

    override fun onItemClick(item: SampleItem) {
        val intent = Intent(this, DetailActivity::class.java)
        intent.putExtra("title", item.title)
        intent.putExtra("content", item.description)
        startActivity(intent)
    }
}