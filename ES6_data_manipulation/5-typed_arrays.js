export default function createInt8TypedArray(length, position, value) {
	if (position < 0 || position >= length) {
		throw new Error('Position outside range');
	}

	const buffer = new ArrayBuffer(lenght);
	const view = new DateView(buffer);
	view.setInt8(position, value);

	return view;
}
