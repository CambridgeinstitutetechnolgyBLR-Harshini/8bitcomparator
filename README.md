![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Tiny Tapeout Verilog Project Template
# 8-bit Comparator

## Description
This project implements an 8-bit unsigned comparator using combinational logic.
It compares two 8-bit inputs A and B and produces three output flags:
•⁠  ⁠*EQ*: A is equal to B
•⁠  ⁠*GT*: A is greater than B  
•⁠  ⁠*LT*: A is less than B

## How it Works
The comparator takes two 8-bit inputs through the input pins and 
compares them using combinational logic. Only one output flag 
is HIGH at any time.

## Truth Table

| A        | B        | EQ | GT | LT |
|----------|----------|----|----|----|
| 10101010 | 10101010 | 1  | 0  | 0  |
| 11001100 | 10101010 | 0  | 1  | 0  |
| 00110011 | 10101010 | 0  | 0  | 1  |

## Pin Description

### Inputs
| Pin    | Description        |
|--------|--------------------|
| ui_in  | 8-bit input A      |
| uio_in | 8-bit input B      |

### Outputs
| Pin       | Bit | Description   |
|-----------|-----|---------------|
| uo_out[0] | 0   | EQ flag (A==B)|
| uo_out[1] | 1   | GT flag (A>B) |
| uo_out[2] | 2   | LT flag (A<B) |

## How to Test
Apply any two 8-bit values to ui_in and uio_in.
Check uo_out bits 0, 1, 2 for comparison result.

## External Hardware
None required.

- [Read the documentation for project](docs/info.md)

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Set up your Verilog project

1. Add your Verilog files to the `src` folder.
2. Edit the [info.yaml](info.yaml) and update information about your project, paying special attention to the `source_files` and `top_module` properties. If you are upgrading an existing Tiny Tapeout project, check out our [online info.yaml migration tool](https://tinytapeout.github.io/tt-yaml-upgrade-tool/).
3. Edit [docs/info.md](docs/info.md) and add a description of your project.
4. Adapt the testbench to your design. See [test/README.md](test/README.md) for more information.

The GitHub action will automatically build the ASIC files using [LibreLane](https://www.zerotoasiccourse.com/terminology/librelane/).

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)

## What next?

- [Submit your design to the next shuttle](https://app.tinytapeout.com/).
- Edit [this README](README.md) and explain your design, how it works, and how to test it.
- Share your project on your social network of choice:
  - LinkedIn [#tinytapeout](https://www.linkedin.com/search/results/content/?keywords=%23tinytapeout) [@TinyTapeout](https://www.linkedin.com/company/100708654/)
  - Mastodon [#tinytapeout](https://chaos.social/tags/tinytapeout) [@matthewvenn](https://chaos.social/@matthewvenn)
  - X (formerly Twitter) [#tinytapeout](https://twitter.com/hashtag/tinytapeout) [@tinytapeout](https://twitter.com/tinytapeout)
  - Bluesky [@tinytapeout.com](https://bsky.app/profile/tinytapeout.com)
