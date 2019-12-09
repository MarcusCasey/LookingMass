#ifndef IMAGE_H
#define IMAGE_H

#include <cstdint>
#include <tuple>

using uint = unsigned int;
using ubyte1 = std::uint8_t;
using ubyte2 = std::uint16_t;
using DIMS = std::tuple<uint, uint>;

class Image {
private:
	uint height, width;
	ubyte2 maxGray;
	ubyte2 * pixels;
public:
	Image();
	Image(Image &);
	~Image();
public:
	DIMS getDims() const;
	//void setDims(uint width_, uint height_);

	ubyte2 getMaxGray() const;
	//void setMaxGray(ubyte2 maxGray_);

	ubyte2 & operator()(uint x, uint y);
	const ubyte2 & operator()(uint x, uint y) const;

	void reset();
	void create(uint height_, uint width_, ubyte2 maxGray_);

	Image& operator=(const Image& other);
};

#endif
