/* verilator lint_off UNUSED */
module  top_sim_error (input reg clk_i);

   //logic clk_i;
   import  shunt_dpi_pkg::*;

   logic reset_n;
   logic [31:0] clk_cnt=0;
   time       start_time=0;
   longint    event_cnt=0;
   longint    startTime =0;
   longint    endTime = 0;

   initial   begin
      start_time = $time;
      startTime =  shunt_dpi_gettimeofday_sec();
      event_cnt  = 0;
   end

   always @(posedge clk_i) begin
      $display("Current Time(%0d)  Time(%0t)",shunt_dpi_gettimeofday_sec(),$time);
     if ($time > 1000 ) begin
        dummy
        $finish;//<- syntax error 
     end // if ($time > 200_000 )

   end // always @ (posedge clk_i)

   always @(posedge clk_i) begin
      clk_cnt  <=  clk_cnt_BAD +1;//Error
      if (clk_cnt > 10) reset_n <= 1;
      else  reset_n <= 0;
   end // always @ (posedge clk_i)
$foo
endmodule: top_sim_error
/* verilator lint_on UNUSED */
