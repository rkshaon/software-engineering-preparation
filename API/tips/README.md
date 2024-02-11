# API development tips

Tip #1: **Use clear naming**
- Choose straigth forward name
- Choose logical name

Example

&#x2612; https://example.com/api/v1/cart/123

&#x2611;https://example.com/api/v1/carts/123

Tip #2: **Ensure reliability through idempotent APIs**

An API request is idempotent if sending it multiple times with the same data results in the same outcome as making it just once. Imagine a light switch: flipping it repeatedly doesn't change the state (on or off).
This concept is reliable for APIs.

<table>
  <tr>
    <th colspan="2">Idempotence</th>
  </tr>
  <tr>
    <th>HTTP Method</th>
    <th>Idempotence</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>No</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>PUT</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>PATCH</td>
    <td>No</td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>Yes</td>
  </tr>
</table>

Tip #3: **Add versioning**
- https://example.com/api/v1/carts/123
- https://example.com/api/v2/carts/123

Versioning allows updating APIs while supporting backward compatibility. This lets developers using the old versions upgrade on their own timeline. This requires well-documented release note.

Tip #4: **Add pagination**

Tip #5: **Use clear query string for sorting and filtering API data**

Tip #6: **Don't make security an afterthought when designing APIs**

Tip #7: **Keep cross-resource references simple**

Example

&#x2611; https://example.com/api/v1/carts/123/items/321

&#x2612; https://example.com/api/v1/items?cart_id=123&item_id=321

Tip #8: **Plan for rate limiting**





[Resource](https://youtu.be/_gQaygjm_hg?si=hwPw8h9z3cBm7i5h)
