function updateQuantity(button, change) {
    // 取得input的值
    const quantityInput = button.parentElement.querySelector('input[name="quantity"]');
    let currentQuantity = parseInt(quantityInput.value);
    
    // 計算新的數量
    let newQuantity = currentQuantity + change;
    
    // 確保數量在範圍內
    if (newQuantity < 1) {
        newQuantity = 1;
    }
    if (newQuantity > 9) {
        newQuantity = 9;
    }
    
    // 更新输入框的值
    quantityInput.value = newQuantity;
    
    // 更新隐藏的表單數入框的值
    const addToCartForm = button.closest('.product-item').querySelector('form');
    if (addToCartForm) {
        const hiddenQuantityInput = addToCartForm.querySelector('.quantity-input');
        if (hiddenQuantityInput) {
            hiddenQuantityInput.value = newQuantity;
        } else {
            console.error('Hidden quantity input not found');
        }
    } else {
        console.error('Form not found');
    }
}