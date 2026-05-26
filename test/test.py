# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    """Test A == B"""
    dut.ui_in.value  = 0b10101010   # A = 170
    dut.uio_in.value = 0b10101010   # B = 170
    dut.ena.value = 1
    dut.rst_n.value = 1
    await Timer(10, units="ns")

    assert dut.uo_out.value & 0x01, "EQ flag should be 1"
    assert not (dut.uo_out.value & 0x02), "GT flag should be 0"
    assert not (dut.uo_out.value & 0x04), "LT flag should be 0"

@cocotb.test()
async def test_comparator_greater(dut):
    """Test A > B"""
    dut.ui_in.value  = 200   # A
    dut.uio_in.value = 100   # B
    dut.ena.value = 1
    dut.rst_n.value = 1
    await Timer(10, units="ns")

    assert not (dut.uo_out.value & 0x01), "EQ should be 0"
    assert dut.uo_out.value & 0x02,       "GT should be 1"
    assert not (dut.uo_out.value & 0x04), "LT should be 0"

@cocotb.test()
async def test_comparator_less(dut):
    """Test A < B"""
    dut.ui_in.value  = 50    # A
    dut.uio_in.value = 200   # B
    dut.ena.value = 1
    dut.rst_n.value = 1
    await Timer(10, units="ns")

    assert not (dut.uo_out.value & 0x01), "EQ should be 0"
    assert not (dut.uo_out.value & 0x02), "GT should be 0"
    assert dut.uo_out.value & 0x04,       "LT should be 1"

@cocotb.test()
async def test_comparator_random(dut):
    """Random tests"""
    dut.ena.value = 1
    dut.rst_n.value = 1

    for _ in range(20):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        dut.ui_in.value  = a
        dut.uio_in.value = b
        await Timer(10, units="ns")

        eq = (dut.uo_out.value & 0x01) != 0
        gt = (dut.uo_out.value & 0x02) != 0
        lt = (dut.uo_out.value & 0x04) != 0

        assert eq == (a == b), f"EQ wrong for A={a} B={b}"
        assert gt == (a  > b), f"GT wrong for A={a} B={b}"
        assert lt == (a  < b), f"LT wrong for A={a} B={b}"
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 50

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
