// HelloWorld.sv
module HelloWorld;
   
 
   
  // This initial block will be executed at the start of the simulation
  initial begin
    int seed;
    int delay;
    
    // Check if a seed value is provided via command line arguments
    if (!$value$plusargs("seed=%d", seed)) begin
      $display("No seed provided, using default seed.");
      seed = $urandom; // Use a default seed if none is provided
    end
    
    // Initialize the random seed
    $urandom(seed);
    
    // Generate a random delay between 1 and 10
     delay = 1;  //$urandom_range(1, 10);

      
    $display("Starting simulation with a delay of %0d time units.", delay);
    
    // Wait for the random delay
    //#delay ;
    
    // Print "Hello, World!"
    $display("Hello, World!");
    
    $finish; // Terminate the simulation
  end

endmodule // HelloWorld


