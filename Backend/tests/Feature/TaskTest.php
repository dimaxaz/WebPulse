<?php

namespace Tests\Feature;

use Tests\TestCase;
use App\Models\Task;
use Illuminate\Foundation\Testing\RefreshDatabase;

class TaskTest extends TestCase
{
    use RefreshDatabase;

    public function test_can_get_tasks()
    {
        Task::factory()->count(3)->create();
        $response = $this->getJson('/api/tasks');
        $response->assertStatus(200)->assertJsonCount(3);
    }

    public function test_can_create_task()
    {
        $data = ['title' => 'New Task', 'description' => 'Task Description'];
        $response = $this->postJson('/api/tasks', $data);
        $response->assertStatus(201)->assertJsonFragment($data);
    }
}
